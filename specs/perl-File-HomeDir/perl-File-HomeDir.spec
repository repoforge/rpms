# $Id$
# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-HomeDir

Summary: Get the home directory of a user
Name: perl-File-HomeDir
Version: 0.64
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-HomeDir/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/File-HomeDir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
With this module, you can get the home directory of a user.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/File/HomeDir.pm
%{perl_vendorlib}/File/HomeDir/Darwin.pm
%{perl_vendorlib}/File/HomeDir/MacOS9.pm
%{perl_vendorlib}/File/HomeDir/Unix.pm
%{perl_vendorlib}/File/HomeDir/Windows.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Updated to release 0.64.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Updated to release 0.62.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
