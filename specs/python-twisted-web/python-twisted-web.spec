# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name TwistedWeb

Summary: Twisted web server, programmable in Python
Name: python-twisted-web
Version: 8.2.0
Release: 1%{?dist}
License: MIT
Group: Development/Libraries
URL: http://twistedmatrix.com/trac/wiki/TwistedWeb

Source: http://tmrc.mit.edu/mirror/twisted/Web/8.2/TwistedWeb-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: python-twisted-core
Requires: python-soap
Requires: python-twisted-core

%description
Twisted is an event-based framework for internet applications.

Twisted Web is a complete web server, aimed at hosting web
applications using Twisted and Python, but fully able to serve static
pages, also.

%prep
%setup -n %{real_name}-%{version}

%{__sed} -i -e '/^#! *\/usr\/bin\/python/d' twisted/web/test/test_cgi.py
%{__sed} -i -e '/^#! *\/usr\/bin\/python/d' twisted/web/test/test_distrib.py

%build
%{__python} setup.py build 

%install
%{__rm} -rf %{buildroot}
### Put into same arch-directory as python-twisted-core
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --install-purelib="%{python_sitearch}"

%clean
%{__rm} -rf %{buildroot}

%post -p %{_libexecdir}/twisted-dropin-cache
%postun -p %{_libexecdir}/twisted-dropin-cache

%files
%defattr(-, root, root, 0755)
%doc LICENSE NEWS README doc/*
%{python_sitearch}/twisted/web/
%{python_sitearch}/twisted/plugins/twisted_web.py*

%changelog
* Mon Apr 23 2012 Steve Huff <shuff@vecna.org> - 8.2.0-1
- Update to 8.2.0.

* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 8.1.0-1
- Initial package. (based on fedora)
