# $Id$
# Authority: dries
# Upstream: Stephanie Wehner <_$r4k,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name NetPacket

Summary: Assemble and dissassemble network packets
Name: perl-NetPacket
Version: 0.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NetPacket/

Source: http://www.cpan.org/modules/by-module/NetPacket/NetPacket-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
These modules do basic disassembly of network packets of various Internet 
protocols.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/NetPacket.pm
%{perl_vendorlib}/NetPacket/

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
