# $Id:$
# Authority: cmr
# Upstream: lasso-devel@lists.labs.libre-entreprise.org
# ExclusiveDist: el5

%define perl_archlib %(eval "`%{__perl} -V:archlib`"; echo $archlib)
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%{?el5:%define php_libdir %{_libdir}/php/}

Name:		lasso
Version:	2.2.2
Release:	1%{?dist}
Summary:	free software C library aiming to implement the Liberty Alliance standards

Group:		Application/System	
License:	GPL
URL:		http://lasso.entrouvert.org/
Source0:	https://labs.libre-entreprise.org/frs/download.php/735/lasso-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	expat-devel
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	make	
BuildRequires:	openssl-devel
BuildRequires:	php-devel
%{?el5:BuildRequires:	python-devel}
%{?el5:BuildRequires:	python-elementtree}
%{?el5:BuildRequires:	swig}
BuildRequires:	xmlsec1-devel	
BuildRequires:	xmlsec1-openssl-devel	
Requires:	expat
Requires:	glib2
Requires:	libxml2
Requires:	openssl
Requires:	php
Requires:	xmlsec
Requires:	xmlsec-openssl

%description
Lasso is a free software C library aiming to implement the Liberty Alliance standards; it defines processes for federated identities, single sign-on and related protocols. Lasso is built on top of libxml2, XMLSec and OpenSSL and is licensed under the GNU General Public License  (with an OpenSSL exception). 

%package -n perl-lasso
Summary: perl bindings for lasso
Group:   Application/System
Requires: lasso = %{version}

%description -n perl-lasso
perl bindings for lasso

%package -n python-lasso
Summary: python bindings for lasso
Group:   Application/System
Requires: lasso = %{version}
Requires: python
Requires: python-elementree

%description -n python-lasso
python bindings for lasso

%package -n php-lasso
Summary: php bindings for lasso
Group:   Application/System
Requires: lasso = %{version}
Requires: php

%description -n php-lasso
php bindings for lasso

%prep
%setup -q

%build
%configure \
	--enable-php5 \
	--with-php5-config-dir=/etc/php.d
make MAKE_PL_OPTS="INSTALLDIRS=\"vendor\"" PREFIX="%{buildroot}%{_prefix}" 


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{_libdir}/liblasso.a
%{__rm} -f %{buildroot}%{_libdir}/liblasso.la
%{__rm} -f %{buildroot}%{_libdir}/php/modules/lasso.a
%{__rm} -f %{buildroot}%{_libdir}/php/modules/lasso.la

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc %{_defaultdocdir}/lasso
%{_libdir}/liblasso.so
%{_libdir}/liblasso.so.3
%{_libdir}/liblasso.so.3.7.1
%{_libdir}/pkgconfig/lasso.pc
%{_includedir}/lasso

%files -n perl-lasso
%{perl_vendorarch}/auto/lasso/.packlist
%{perl_vendorarch}/auto/lasso/lasso.bs
%{perl_vendorarch}/auto/lasso/lasso.so
%{perl_vendorarch}/lasso.pm

%files -n python-lasso
%{python_sitearch}/_lasso.a
%{python_sitearch}/_lasso.la
%{python_sitearch}/_lasso.so
%{python_sitearch}/lasso.py
%{python_sitearch}/lasso.pyc
%{python_sitearch}/lasso.pyo

%files -n php-lasso
%{_sysconfdir}/php.d/lasso.ini
%{_libdir}/php/modules/lasso.so
%{_datadir}/php/lasso.php



%changelog
