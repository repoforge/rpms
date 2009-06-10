# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Unihan

Summary: Perl module that implements the Unihan Data Base
Name: perl-Unicode-Unihan
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Unihan/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Unihan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unicode-Unihan is a Perl module that implements the Unihan Data Base.

This package contains the following Perl module:

    Unicode::Unihan

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
%doc Changes MANIFEST META.yml NOTES README
%doc %{_mandir}/man3/Unicode::Unihan.3pm*
%dir %{perl_vendorlib}/Unicode/
%{perl_vendorlib}/Unicode/Unihan/
%{perl_vendorlib}/Unicode/Unihan.pm

%changelog
* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
