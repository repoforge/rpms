# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Lint-like tool for Python
Name: pyflakes
Version: 0.2.1
Release: 1%{?dist}
License: MIT
Group: Development/Languages
URL: http://divmod.org/trac/wiki/DivmodPyflakes

Source: http://divmod.org/static/projects/pyflakes/pyflakes-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 2.3

%description
PyFlakes is a Lint-like tool for Python, like PyChecker. It is focused on
identifying common errors quickly without executing Python code. Its primary
advantage over PyChecker is that it is fast. You don't have to sit around
for minutes waiting for the checker to run; it runs on most large projects in
only a few seconds.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
 
%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_bindir}/pyflakes
%{python_sitelib}/pyflakes/
%ghost %{python_sitelib}/pyflakes/*.pyo

%changelog
* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Initial package. (using DAR)
