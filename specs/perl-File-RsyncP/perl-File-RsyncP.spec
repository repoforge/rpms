# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-RsyncP

Summary: Implementation of an Rsync client
Name: perl-File-RsyncP
Version: 0.52
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-RsyncP/

Source: http://www.cpan.org/modules/by-module/File/File-RsyncP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
File::RsyncP is a perl implementation of an Rsync client.  It is
compatible with Rsync 2.5.5 (protocol version 26).  It can send
or receive files, either by running rsync on the remote machine,
or connecting to an rsyncd deamon on the remote machine.

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
        PREFIX="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST LICENSE README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/*

%changelog
* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.52-1
- Initial package. (using DAR)
