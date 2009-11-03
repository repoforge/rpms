# $Id$
# Authority: dag
# Upstream: Struan Donald <struan$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-FormatText-WithLinks

Summary: HTML to text conversion with links as footnotes
Name: perl-HTML-FormatText-WithLinks
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-FormatText-WithLinks/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-FormatText-WithLinks-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More)

%description
HTML to text conversion with links as footnotes.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/HTML::FormatText::WithLinks.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/HTML/
%dir %{perl_vendorlib}/HTML/FormatText/
#%{perl_vendorlib}/HTML/FormatText/WithLinks/
%{perl_vendorlib}/HTML/FormatText/WithLinks.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
