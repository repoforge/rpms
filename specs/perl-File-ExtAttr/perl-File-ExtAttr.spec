# $Id$
# Authority: dag
# Upstream: Richard Dawe <richdawe$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-ExtAttr

Summary: Perl module for accessing extended attributes of files
Name: perl-File-ExtAttr
Version: 1.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-ExtAttr/

Source: http://www.cpan.org/modules/by-module/File/File-ExtAttr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: libattr-devel
Requires: perl

%description
File-ExtAttr is a Perl module for accessing extended attributes of files.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/File::ExtAttr.3pm*
%doc %{_mandir}/man3/File::ExtAttr::Tie.3pm*
%dir %{perl_vendorarch}/File/
%{perl_vendorarch}/File/ExtAttr.pm
%{perl_vendorarch}/File/ExtAttr/
%dir %{perl_vendorarch}/auto/File/
%{perl_vendorarch}/auto/File/ExtAttr/

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
