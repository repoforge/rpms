# $Id: $

# Authority: dries
# Upstream:

%define real_name HTML-Clean

Summary: Cleans HTML
Name: perl-HTML-Clean
Version: 0.8
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Clean/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/L/LI/LINDNER/HTML-Clean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The HTML::Clean module encapsulates a number of HTML optimizations
and cleanups.  The end result is HTML that loads faster, displays
properly in more browsers.  Think of it as a compiler that
translates HTML input into optimized machine readable code.

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
%{_bindir}/htmlclean
%{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/auto/HTML/Clean/autosplit.ix
%{_libdir}/perl5/vendor_perl/*/HTML/Clean.pm
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
