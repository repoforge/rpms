# $Id$
# Authority: dries
# Upstream: Chip Turner <cturner$redhat,com>

%define real_name RPM-Specfile

Summary: Perl module for creating rpm packages of other perl modules
Name: perl-RPM-Specfile
Version: 1.12
Release: 1.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPM-Specfile/

Source: http://www.cpan.org/modules/by-module/RPM/RPM-Specfile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
Requires: perl
BuildRequires: perl

%description
Simple module for creation of RPM Spec files.  Used by cpanflute2 to turn CPAN
tarballs into RPM modules.
See the included script cpanflute2 for usage; documentation coming soon.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1.2
- Rebuild for Fedora Core 5.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 1.12-1
- Fixed site -> vendor. (Matthew Mastracci)

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.12-0
- Updated to release 1.12.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 1.11-0
- Initial package. (using DAR)
