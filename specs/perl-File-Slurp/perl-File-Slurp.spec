# $Id: $

# Authority: dries
# Upstream:

%define real_name File-Slurp

Summary: Efficient reading and writing of complete files
Name: perl-File-Slurp
Version: 9999.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Slurp/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/U/UR/URI/File-Slurp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module provides subroutines to read or write entire files with a
simple call.  It also has a subroutine for reading the list of filenames
in a directory.

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
%doc README Changes
%{_mandir}/man3/*
%{_libdir}/perl5/vendor_perl/*/File/Slurp.pm
# %{_libdir}/perl5/vendor_perl/*/File/Slurp/*
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 9999.04
- Initial package.
