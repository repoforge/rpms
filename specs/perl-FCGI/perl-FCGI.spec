# $Id: $

# Authority: dries
# Upstream:

%define real_name FCGI

Summary: Fast CGI module
Name: perl-FCGI
Version: 0.67
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FCGI/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/S/SK/SKIMO/FCGI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This is a Fast CGI module for perl. It's based on the FCGI module
that comes with Open Market's FastCGI Developer's Kit, but does
not require you to recompile perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README ChangeLog LICENSE.TERMS
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/FCGI.pm
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/FCGI/.packlist
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/FCGI/FCGI.bs
%{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/FCGI/FCGI.so
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Initial package.
