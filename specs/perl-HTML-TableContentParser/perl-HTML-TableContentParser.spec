# $Id$
# Authority: dag
# Upstream: Simon Drabble <sdrabble$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TableContentParser

Summary: Perl module to do interesting things with the contents of tables
Name: perl-HTML-TableContentParser
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-TableContentParser/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-TableContentParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-HTML-TableContentParser is a Perl module to do interesting things
with the contents of tables.

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
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man3/HTML::TableContentParser.3pm*
%dir %{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTML/TableContentParser.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
