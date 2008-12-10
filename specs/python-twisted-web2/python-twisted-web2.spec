# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name TwistedWeb2

Summary: Twisted web server, programmable in Python
Name: python-twisted-web2
Version: 0.6.1
Release: 1
License: MIT
Group: Development/Libraries
URL: http://twistedmatrix.com/trac/wiki/TwistedWeb

Source: http://tmrc.mit.edu/mirror/twisted/Web2/0.6/TwistedWeb2-%{version}.tar.bz2
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

%{__sed} -i -e '/^#! *\/usr\/bin\/python/d' twisted/web2/test/test_cgi.py

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
%{python_sitearch}/twisted/web2/
%{python_sitearch}/twisted/plugins/twisted_web2.py*

%changelog
* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Initial package. (based on fedora)
