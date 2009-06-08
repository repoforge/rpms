# $Id$
# Authority: dag
# Upstream: Lyo Kato <lyo,kato$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UTF8BOM

Summary: Perl module for handling Byte Order Mark for UTF-8 files
Name: perl-UTF8BOM
Version: 1.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UTF8BOM/

Source: http://www.cpan.org/authors/id/L/LY/LYOKATO/UTF8BOM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UTF8BOM is a Perl module for handling Byte Order Mark for UTF-8 files.

This package contains the following Perl module:

    UTF8BOM

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man1/utf8bom.1*
%doc %{_mandir}/man3/UTF8BOM.3pm*
%{_bindir}/utf8bom
%{perl_vendorlib}/UTF8BOM.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.02-1
- Updated to version 1.02.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Initial package. (using DAR)
