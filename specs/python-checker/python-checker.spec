# $Id$
# Authority: dries
# Upstream: Neal Norwitz <neal$metaslash,com>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define real_name pychecker

Summary: Find common bugs in Python source code
Name: python-checker
Version: 0.8.16
Release: 1
License: BSD
Group: Development/Tools
URL: http://pychecker.sourceforge.net/

Source: http://dl.sf.net/pychecker/pychecker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python

%description
PyChecker is a tool for finding common bugs in Python source code. It finds 
problems that are typically caught by a compiler (or lint) for less dynamic 
languages, like C and C++. Common errors that can be found include forgetting 
to import a module, misspelling a variable, passing the wrong number of 
parameters to a function/method, and not using a module/variable.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

#FIXME
%{__perl} -pi -e "s|%{buildroot}||g;" %{buildroot}%{_bindir}/pychecker

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG KNOWN_BUGS MAINTAINERS README TODO
%{_bindir}/pychecker
%dir %{python_sitearch}/pychecker
%{python_sitearch}/pychecker/*.py*
%exclude %{python_sitearch}/pychecker/CHANGELOG
%exclude %{python_sitearch}/pychecker/COPYRIGHT
%exclude %{python_sitearch}/pychecker/KNOWN_BUGS
%exclude %{python_sitearch}/pychecker/MAINTAINERS
%exclude %{python_sitearch}/pychecker/README
%exclude %{python_sitearch}/pychecker/TODO
%exclude %{python_sitearch}/pychecker/VERSION

%changelog
* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.16-1
- Initial package.
