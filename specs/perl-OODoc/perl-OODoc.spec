# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name OODoc

Summary: Creates code related documentation
Name: perl-OODoc
Version: 1.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/OODoc/

Source: http://www.cpan.org/modules/by-module/OODoc/OODoc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Creates code related documentation in an object oriented way.

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
%doc ChangeLog LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man1/oodist.1*
%doc %{_mandir}/man3/OODoc.3pm*
%doc %{_mandir}/man3/OODoc::*.3pm*
%{_bindir}/oodist
%{perl_vendorlib}/OODoc/
%{perl_vendorlib}/OODoc.pm
%{perl_vendorlib}/OODoc.pod

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 1.01-1
- Updated to latest upstream version { old source not available }

* Wed Jan 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Updated to release 0.98.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
