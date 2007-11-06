# $Id$
# Authority: matthias

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-AIO

Summary: Asynchronous Input/Output
Name: perl-IO-AIO
Version: 2.33
Release: 1
License: Artistic or GPL
Group: Development/Libraries
URL: http://search.cpan.org/~mlehmann/IO-AIO/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/IO-AIO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Provided by either perl or perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements asynchronous I/O using whatever means your operating
system supports.


%prep
%setup -n %{real_name}-%{version}


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod \
           %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README
%dir %{perl_vendorarch}/IO/
%{perl_vendorarch}/IO/AIO.pm
%dir %{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/auto/IO/AIO/
%{_mandir}/man3/*.3pm*


%changelog
* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 2.33-1
- Update to 2.33.
- Build require perl(ExtUtils::MakeMaker) for F7.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.73-1
- Initial RPM release.
- Not sure if the autoconf.pm should be included or not...

