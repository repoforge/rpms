# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%define real_name MailTools

Summary: MailTools module for perl 
Name: perl-MailTools
Version: 1.64
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MailTools/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/MailTools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: perl-Mail

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
%{?rh7:BuildRequires: perl-libnet >= 1.05}
Requires: perl >= 0:5.00503
%{?rh7:BuildRequires: perl-libnet >= 1.05}

%description
MailTools module for perl

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
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
%doc README* ChangeLog
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.64-0
- Updated to release 1.64.

* Fri Nov 28 2003 Dag Wieers <dag@wieers.com> - 1.60-0
- Updated to release 1.60.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.58-0
- Updated to release 1.58.

* Sun Jan 23 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
