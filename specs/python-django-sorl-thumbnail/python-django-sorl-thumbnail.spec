# $Id$
# Authority: yury
# Upstream: Mikko Hellsing <mikko$aino,se>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%define real_name sorl-thumbnail

Name: python-django-sorl-thumbnail
Version: 11.09
Release: 1%{?dist}
Summary: Thumbnails for Django
Group: Development/Languages
License: BSD
URL: https://github.com/sorl/sorl-thumbnail

Source0: http://pypi.python.org/packages/source/s/%{real_name}/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.5
BuildRequires: python-setuptools
BuildRequires: python-sphinx

Requires: python-django
Requires: python-imaging

Requires: ImageMagick

%description
Thumbnails for Django. Totally rewritten.

%prep
%setup -n %{real_name}-%{version}

%if 0%{?el6}
    %{__sed} -i -e "s/, 'sphinx.ext.viewcode'//" docs/conf.py
    %{__sed} -i -e 's/nature/default/' docs/conf.py
%endif

%build
%{__python} setup.py build

make -C docs html
mv docs/_build/html htmldocs
rm -rf docs
rm -f htmldocs/.buildinfo

%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc LICENSE PKG-INFO README.rst
%doc htmldocs
%{python_sitelib}/sorl/*.py*
%{python_sitelib}/sorl/thumbnail/
%{python_sitelib}/*.egg-info

%changelog
* Mon Oct 03 2011 Yury V. Zaytsev <yury@shurup.com> - 11.09-1
- Updated to release 11.09.

* Fri Sep 09 2011 Yury V. Zaytsev <yury@shurup.com> - 11.05.2-1
- Initial package.
