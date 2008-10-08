# $Id$
# Authority: dag
# Upstream: Sisyphus <sisyphus$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FileHandle-Fmode

Summary: Perl module to determine whether a filehandle is opened for reading, writing, or both
Name: perl-FileHandle-Fmode
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FileHandle-Fmode/

Source: http://www.cpan.org/modules/by-module/FileHandle/FileHandle-Fmode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-FileHandle-Fmode is a Perl module to determine whether a filehandle
is opened for reading, writing, or both

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/FileHandle::Fmode.3pm*
%dir %{perl_vendorarch}/auto/FileHandle/
%{perl_vendorarch}/auto/FileHandle/Fmode/
%dir %{perl_vendorarch}/FileHandle/
%{perl_vendorarch}/FileHandle/Fmode.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
