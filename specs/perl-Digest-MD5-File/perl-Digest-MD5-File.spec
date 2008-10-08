# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-MD5-File

Summary: Perl extension for getting MD5 sums for files and urls
Name: perl-Digest-MD5-File
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-MD5-File/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-MD5-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension for getting MD5 sums for files and urls.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Digest::MD5::File.3pm*
%dir %{perl_vendorlib}/Digest/
%dir %{perl_vendorlib}/Digest/MD5/
#%{perl_vendorlib}/Digest/MD5/File/
%{perl_vendorlib}/Digest/MD5/File.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
