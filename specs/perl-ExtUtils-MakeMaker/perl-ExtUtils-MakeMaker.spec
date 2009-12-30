# $Id$
# Authority: dag
# Upstream: Michael G Schwern <schwern$pobox,com>

# ExclusiveDist: el2 rh7 rh9 el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-MakeMaker

Summary: Create a module Makefile
Name: perl-ExtUtils-MakeMaker
Version: 6.56
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-MakeMaker/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(DirHandle)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec) >= 0.8
BuildRequires: perl(Pod::Man)
BuildRequires: perl >= 5.006
Requires: perl(DirHandle)
Requires: perl(File::Basename)
Requires: perl(File::Spec) >= 0.8
Requires: perl(Pod::Man)
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup


%description
This is a CPAN distribution of the venerable MakeMaker module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} 

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml NOTES README TODO
%doc %{_mandir}/man1/instmodsh.1*
%doc %{_mandir}/man3/ExtUtils::*.3pm*
%{_bindir}/instmodsh
%{perl_vendorlib}/ExtUtils/

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 6.56-1
- Updated to version 6.56.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 6.54-1
- Updated to version 6.54.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 6.52-1
- Updated to version 6.52.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 6.46-1
- Updated to release 6.46.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 6.44-1
- Updated to release 6.44.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 6.42-1
- Updated to release 6.42.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 6.40-1
- Updated to release 6.40.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 6.38-1
- Updated to release 6.38.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 6.36-1
- Updated to release 6.36.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 6.30-1
- Updated to release 6.30.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 6.17-1
- Initial package. (using DAR)
