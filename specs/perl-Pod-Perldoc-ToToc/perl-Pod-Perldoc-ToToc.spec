# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Pod-Perldoc-ToToc

Summary: Turn one or more Pod files into a table of contents
Name: perl-Pod-Perldoc-ToToc
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Pod-Perldoc-ToToc/

Source: http://www.cpan.org/modules/by-module/Pod/Pod-Perldoc-ToToc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Translates Pod to a table of contents.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Pod::Perldoc::ToToc.3*
%doc %{_mandir}/man3/Pod::TOC.3*
%dir %{perl_vendorlib}/Pod/
%dir %{perl_vendorlib}/Pod/Perldoc/
#%{perl_vendorlib}/Pod/Perldoc/ToToc/
%{perl_vendorlib}/Pod/Perldoc/ToToc.pm
%{perl_vendorlib}/Pod/TOC.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.09-1
- Updated to version 1.09.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Wed Jan 10 2007 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
