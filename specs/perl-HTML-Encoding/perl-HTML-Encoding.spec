# $Id$
# Authority: dag
# Upstream: Bjoern Hoehrmann <bjoern$hoehrmann,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Encoding

Summary: Determine the encoding of HTML/XML/XHTML documents
Name: perl-HTML-Encoding
Version: 0.60
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Encoding/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Encoding-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Determine the encoding of HTML/XML/XHTML documents.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/HTML::Encoding.3pm*
%dir %{perl_vendorlib}/HTML/
#%{perl_vendorlib}/HTML/Encoding/
%{perl_vendorlib}/HTML/Encoding.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.60-1
- Updated to release 0.60.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.57-1
- Updated to release 0.57.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.56-1
- Updated to release 0.56.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.53-1
- Initial package. (using DAR)
