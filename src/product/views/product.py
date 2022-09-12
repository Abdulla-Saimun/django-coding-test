from django.views import generic

from product.models import Variant, ProductVariantPrice, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.fliters import ProductFilter


class CreateProductView(generic.TemplateView):
    template_name = "products/create.html"

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values("id", "title")
        context["product"] = True
        context["variants"] = list(variants.all())
        return context


class ListProductView(generic.ListView):
    paginate_by = 10
    model = ProductVariantPrice
    template_name = "products/list.html"

    def get_context_data(self, **kwargs):
        product = Product.objects.all()
        queryList = []
        for pr in product:
            Query = ProductVariantPrice.objects.filter(product__title=pr.title)
            queryList.append(Query)
        print(len(queryList))
        context = super(ListProductView, self).get_context_data(**kwargs)
        list_Product = ProductVariantPrice.objects.all()
        paginator = Paginator(list_Product, self.paginate_by)
        page = self.request.GET.get("page")
        # print(paginator.num_pages)
        myFilter = ProductFilter(self.request.GET, queryset=self.queryset)

        try:
            prod_list = paginator.page(page)  # type: ignore
            print(prod_list)
        except PageNotAnInteger:
            prod_list = paginator.page(1)
        except EmptyPage:
            prod_list = paginator.page(paginator.num_pages)

        context["list_product"] = prod_list
        context["rng"] = range(paginator.num_pages)
        context["objCount"] = list_Product.count
        context["myFilter"] = myFilter
        context["products"] = product
        context["queryList"] = queryList
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ProductFilter(self.request.GET, queryset=queryset).qs
