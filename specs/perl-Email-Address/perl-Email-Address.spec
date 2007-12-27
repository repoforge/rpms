# $Id$
# Authority: dries
# Upstream: Casey West <casey$geeknest,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Address

Summary: RFC 2822 Address Parsing and Creation
Name: perl-Email-Address
Version: 1.889
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Address/

Source: http://www.cpan.org/modules/by-module/Email/Email-Address-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This class implements a complete RFC 2822 parser that locates email
addresses in strings and returns a list of "Email::Address" objects
found. Alternatley you may construct objects manually. The goal of this
software is to be correct, and very very fast.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Email::Address.3pm*
%dir %{perl_vendorlib}/Email/
#%{perl_vendorlib}/Email/Address/
%{perl_vendorlib}/Email/Address.pm

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.889-1
- Updated to release 1.889.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.888-1
- Updated to release 1.888.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.887-1
- Updated to release 1.887.

* Sun Dec 10 2006 Dries Verachtert <dries@ulyssis.org> - 1.884-1
- Updated to release 1.884.

* Sun Jan  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Initial package.
