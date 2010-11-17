# $Id$
# Authority: dries
# Upstream: Ken Williams <kwilliams$cpan,or>

### EL6 ships with perl-ExtUtils-CBuilder-0.27-115.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-CBuilder
%define real_version 0.260301

Summary: Compile and link C code for Perl modules
Name: perl-ExtUtils-CBuilder
Version: 0.2603.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-CBuilder/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-CBuilder-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Cwd)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(Text::ParseWords)


%description
With this perl module, you can compile and link C code for perl modules

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes INSTALL MANIFEST META.yml README 
%doc %{_mandir}/man3/ExtUtils::CBuilder.3pm*
%doc %{_mandir}/man3/ExtUtils::CBuilder::Platform::Windows.3pm*
%dir %{perl_vendorlib}/ExtUtils/
%{perl_vendorlib}/ExtUtils/CBuilder/
%{perl_vendorlib}/ExtUtils/CBuilder.pm

%changelog
* Mon Aug 14 2009 Christoph Maser <cmr@financial.com> - 0.2603.01-1
- Updated to version 0.2603.01.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.2603-1
- Updated to version 0.2603.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.2602-1
- Updated to version 0.2602.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.24-1
- Updated to release 0.24.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.23-1
- Updated to release 0.23.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Wed Jan 19 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
