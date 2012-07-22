/*	--*- c++ -*--
 * Copyright (C) 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 3 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifdef HAVE_CONFIG_H
#  include <config.h>
#endif

#include <string>
#include <list>
#include <map>
#include <iostream>

class node {
    public:
	node(std::string const &name) : name_(name) {}
	void	add_child(class node *n)
	{
		children_.push_back(n);
	}

	void	dfs(std::list<std::string> &res);
	bool				visited;

    private:
	std::string const		name_;
	std::list<class node *>		children_;
};

void node::dfs(std::list<std::string> &res)
{
	std::list<class node *>::iterator	i;

	visited = true;

	for (i = children_.begin(); i != children_.end(); ++i) {
		if ((*i)->visited)
			continue;

		(*i)->dfs(res);
	}

	res.push_front(name_);
}

int main(void)
{
	std::map<std::string, class node *>		nodes;

	for (;;) {
		std::string		name;
		class node		*cur_node;

		std::cin >> name;
		if (!std::cin.good())
			break;

		if (nodes.find(name) == nodes.end())
			nodes[name] = new node(name);

		cur_node = nodes[name];

		while (std::cin.good()) {
			std::cin >> name;

			if (name == "##")
				break;

			if (nodes.find(name) == nodes.end())
				nodes[name] = new node(name);

			cur_node->add_child(nodes[name]);
		}
	}

	typedef std::map<std::string, class node *>::iterator	node_iterator;

	for (node_iterator n = nodes.begin(); n != nodes.end(); ++n) {
		for (node_iterator m = nodes.begin();
		     m != nodes.end(); ++m)
			m->second->visited = false;

		std::list<std::string>		res(nodes.size());
		n->second->dfs(res);

		for (std::list<std::string>::const_iterator i = res.begin();
		     i != res.end(); ++i)
			std::cout << *i << " ";

		std::cout << std::endl;
	}
}
