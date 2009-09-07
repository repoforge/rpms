# $Id$
# Authority: dag
# Upstream: Jerrad Pierce <jpierce$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RSSLite

Summary: Lightweight, "relaxed" RSS (and XML-ish) parser
Name: perl-XML-RSSLite
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RSSLite/

Source: http://www.cpan.org/modules/by-module/XML/XML-RSSLite-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Lightweight, "relaxed" RSS (and XML-ish) parser.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST README TODO
%doc %{_mandir}/man3/XML::RSSLite.3pm*
%dir %{perl_vendorlib}/XML/
#%{perl_vendorlib}/XML/RSSLite/
%{perl_vendorlib}/XML/RSSLite.pm

%changelog
* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 0.15-1
- Updated to version 0.15.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
