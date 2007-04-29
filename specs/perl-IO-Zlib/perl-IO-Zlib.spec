# $Id$

# Authority: dries
# Upstream: Tom Hughes <tom$compton,nu>

%define real_name IO-Zlib
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: IO:: interface to Compress::Zlib
Name: perl-IO-Zlib
Version: 1.05
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Zlib/

Source: http://www.cpan.org/modules/by-module/IO/IO-Zlib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This modules provides an IO:: style interface to the Compress::Zlib
package. The main advantage is that you can use an IO::Zlib object
in much the same way as an IO::File object so you can have common
code that doesn't know which sort of file it is using.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/IO/Zlib.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
