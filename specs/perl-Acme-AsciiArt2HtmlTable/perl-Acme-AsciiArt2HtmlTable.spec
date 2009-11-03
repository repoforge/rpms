# $Id$
# Authority: dag
# Upstream: José Alves de Castro <cog$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-AsciiArt2HtmlTable

Summary: Perl module to convert Ascii art to an HTML table
Name: perl-Acme-AsciiArt2HtmlTable
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-AsciiArt2HtmlTable/

Source: http://www.cpan.org/modules/by-module/Acme/Acme-AsciiArt2HtmlTable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Acme-AsciiArt2HtmlTable is a Perl module to convert Ascii art to an HTML table.

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
%doc %{_mandir}/man3/Acme::AsciiArt2HtmlTable.3pm*
%dir %{perl_vendorlib}/Acme/
%{perl_vendorlib}/Acme/AsciiArt2HtmlTable.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
