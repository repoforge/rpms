# Authority: dries
# Upstream: Matija Grabnar <matija+pause$serverflow,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Tail

Summary: Perl extension for reading from continuosly updated files
Name: perl-File-Tail
Version: 0.99.3
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Tail/

Source: http://www.cpan.org/modules/by-module/File/File-Tail-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The File::Tail module is designed for reading files which are continously
appended to (the name comes from the tail -f directive). Usualy such files are
logfiles of some description.

The module tries hard not to busy wait on the file, dynamicaly calcultaing
how long it should wait before it pays to try reading the file again.

The module should handle normal log truncations ("close; move; open"
or "cat /dev/null >file") transparently, without losing any input.

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
%doc %{_mandir}/man3/File::Tail.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/Tail/
%{perl_vendorlib}/File/Tail.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.99.3-1
- Updated to release 0.99.3.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.99.1-1
- Updated to release 0.99.1.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 0.98-1
- Changed to noarch package.
- Cleanup and cosmetic changes.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.98-1
- Initial package.
