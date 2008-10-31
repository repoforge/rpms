# $Id$
# Authority: dries
# Upstream: Neal Norwitz <neal$metaslash,com>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Find common bugs in Python source code
Name: pychecker
Version: 0.8.17
Release: 3
License: BSD
Group: Development/Tools
URL: http://pychecker.sourceforge.net/

Source: http://dl.sf.net/pychecker/pychecker-%{version}.tar.gz
Patch0: pychecker-0.8.17-root.patch
Patch1: pychecker-0.8.17-spe.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
Obsoletes: python-checker <= %{version}
BuildRequires: python, python-devel

%description
PyChecker is a tool for finding common bugs in Python source code. It finds
problems that are typically caught by a compiler (or lint) for less dynamic
languages, like C and C++. Common errors that can be found include forgetting
to import a module, misspelling a variable, passing the wrong number of
parameters to a function/method, and not using a module/variable.

%prep
%setup
%patch0 -p1 -b .root
%patch1 -p1 -b .spe

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --root="%{buildroot}" --prefix="%{_prefix}"

### FIXME:
%{__perl} -pi -e "s|%{buildroot}||g;" %{buildroot}%{_bindir}/pychecker

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYRIGHT KNOWN_BUGS MAINTAINERS README TODO VERSION
%{_bindir}/pychecker
%{python_sitelib}/pychecker/
%ghost %{python_sitelib}/pychecker/*.pyo
%exclude %{python_sitelib}/pychecker/CHANGELOG
%exclude %{python_sitelib}/pychecker/COPYRIGHT
%exclude %{python_sitelib}/pychecker/KNOWN_BUGS
%exclude %{python_sitelib}/pychecker/MAINTAINERS
%exclude %{python_sitelib}/pychecker/README
%exclude %{python_sitelib}/pychecker/TODO
%exclude %{python_sitelib}/pychecker/VERSION

%changelog
* Fri Oct 31 2008 Dag Wieers <dag@wieers.com> - 0.8.17-3
- Added Fedora patches.

* Fri Mar 10 2006 Dag Wieers <dag@wieers.com> - 0.8.17-2
- Added .pyo ghost files, renamed to pychecker.

* Mon Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.17-1
- Updated to release 0.8.17.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.16-1
- Initial package.
