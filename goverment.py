class Government:

    @staticmethod
    def unnecessary_stuff(tax: int) -> int:
        return tax - 1000

    def consume(self, tax: int) -> None:
        while True:
            tax = self.unnecessary_stuff(tax)
            if tax < 0:
                break
        return None

    def distribute_two_masks(self, tax: int) -> None:
        return self.consume(tax)


if __name__ == '__main__':
    gov = Government()
    print(gov.fetch_two_masks(100000000000))
