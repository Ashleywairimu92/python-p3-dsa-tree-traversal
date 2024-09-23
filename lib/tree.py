class Tree:
    def __init__(self, structure):
        """Initialize the tree with a given structure."""
        self.structure = structure

    def get_element_by_id(self, element_id):
        """Recursively search for an element by its ID."""
        return self._get_element_by_id_recursive(self.structure, element_id)

    def _get_element_by_id_recursive(self, node, element_id):
        """Helper method to recursively search through the tree."""
        if node.get('id') == element_id:
            return node
        for child in node.get('children', []):
            found = self._get_element_by_id_recursive(child, element_id)
            if found:
                return found
        return None
