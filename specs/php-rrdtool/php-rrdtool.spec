Name:		php-rrdtool
Version:	20051205
Release:	1%{?dist}
Summary:	RRDtool module for PHP

Group:		Development/Languages
License:	GPL
URL:		http://oss.oetiker.ch/rrdtool/
Source0:	http://oss.oetiker.ch/rrdtool/pub/contrib/php_rrdtool.tar.gz
Patch0:		php-rrdtool-libcheck.patch
BuildRoot:	%{_tmppath}/%{name}

BuildRequires:	php-devel
BuildRequires:	rrdtool-devel
BuildRequires:	re2c
BuildRequires:	automake
Requires:	php
Requires:	rrdtool	

%description
The %{name} package includes a dynamic shared object (DSO) that adds
RRDtool bindings to the PHP HTML-embedded scripting language.


%prep
%setup -q -n rrdtool
%patch0 -p1 -b .no-static-lib


%build
phpize
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/lib64/php/modules/rrdtool.so



%changelog
* Mon 29 Dec 2008 Christoph Maser <cmr@financial.com> - 20051205-1
- Initial package
