# $Id$
# Authority: dag
# Upstream: Graciliano Monteiro Passos <gmpassos$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Smart
%define real_version 1.006009

Summary: Smart, easy and powerful way to access/create XML files/data
Name: perl-XML-Smart
Version: 1.6.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Smart/

Source: http://www.cpan.org/modules/by-module/XML/XML-Smart-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A smart, easy and powerful way to access/create XML files/data.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/XML::Smart.3pm*
%doc %{_mandir}/man3/XML::Smart::*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Smart/
%{perl_vendorlib}/XML/Smart.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.6.9-1
- Initial package. (using DAR)
