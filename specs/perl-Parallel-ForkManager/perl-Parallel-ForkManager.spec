# $Id$

# Authority: dag

%define rname Parallel-ForkManager

Summary: Simple parallel processing fork manager.
Name: perl-Parallel-ForkManager
Version: 0.7.5
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parallel-ForkManager/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/D/DL/DLUX/Parallel-ForkManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503


%description
Share Perl variables between processes.

%prep
%setup -n %{rname}-%{version} 

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
%{__rm} -rf %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST TODO
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.7.5-1
- Initial package. (using DAR)
