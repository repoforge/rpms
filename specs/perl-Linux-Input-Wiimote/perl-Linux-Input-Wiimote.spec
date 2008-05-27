# $Id$
# Authority: dag
# Upstream: Chad Phillips <chad$chadphillips,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Linux-Input-Wiimote

Summary: Perl interface to the libcwiimote library
Name: perl-Linux-Input-Wiimote
Version: 0.04002
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Linux-Input-Wiimote/

Source: http://www.cpan.org/modules/by-module/Linux/Linux-Input-Wiimote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libwiimote-devel
BuildRequires: perl
BuildRequires: perl(Test::More)

%description
Perl interface to the libcwiimote library.

%prep
%setup -n %{real_name}-%{version}

%build
#CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" INC="%{_includedir}/libcwiimote/" libpth="%{_libdir}"
#%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
perl Makefile.PL
make

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Linux::Input::Wiimote.3pm*
%dir %{perl_vendorarch}/auto/Linux/
%dir %{perl_vendorarch}/auto/Linux/Input/
%{perl_vendorarch}/auto/Linux/Input/Wiimote/
%dir %{perl_vendorarch}/Linux/
%dir %{perl_vendorarch}/Linux/Input/
%{perl_vendorarch}/Linux/Input/Wiimote.pm

%changelog
* Sat May 24 2008 Dag Wieers <dag@wieers.com> - 0.04002-1
- Initial package. (using DAR)
