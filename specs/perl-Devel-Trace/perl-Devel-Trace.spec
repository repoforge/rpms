# $Id: $

# Authority: dries
# Upstream:

%define real_name Devel-Trace

Summary: Trace perl programs
Name: perl-Devel-Trace
Version: 0.10
Release: 1
License: Unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Trace/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MJ/MJD/Devel-Trace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
If you run your program with "perl -d:Trace program", this module will
print a message to standard error just before each line is executed, like
the "-x" option of bash.

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
%{_libdir}/perl5/vendor_perl/*/Devel/Trace.pm
%exclude %{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/*/i386-linux-thread-multi/auto/Devel/Trace/.packlist

%changelog
* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
