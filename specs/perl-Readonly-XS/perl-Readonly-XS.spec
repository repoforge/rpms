# $Id$
# Authority: dries
# Upstream: Eric J. Roode <sdn,crams20944$zoemail,net>

### EL6 ships with perl-Readonly-XS-1.05-3.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Readonly-XS

Summary: Companion module to Readonly.pm
Name: perl-Readonly-XS
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Readonly-XS/

Source: http://www.cpan.org/modules/by-module/Readonly/Readonly-XS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a companion module to Readonly.pm.  You do not use
Readonly::XS directly.  Instead, once it is installed, Readonly.pm
will detect this and will use it for creating read-only scalars.  This
results in a significant speed improvement.  This does not speed up
read-only arrays or hashes.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Readonly/
%{perl_vendorarch}/Readonly/XS.pm
%dir %{perl_vendorarch}/auto/Readonly/
%{perl_vendorarch}/auto/Readonly/XS/

%changelog
* Mon Jun 22 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
