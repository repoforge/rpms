# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IPC-Shareable

Summary: Share Perl variables between processes
Name: perl-IPC-Shareable
Version: 0.60
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IPC-Shareable/

Source: http://www.cpan.org/modules/by-module/IPC/IPC-Shareable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503


%description
Share Perl variables between processes.

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
%doc CHANGES COPYING CREDITS MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/IPC/Shareable.pm
%{perl_vendorlib}/IPC/Shareable/SharedMem.pm

%changelog
* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.60-1
- Initial package. (using DAR)
