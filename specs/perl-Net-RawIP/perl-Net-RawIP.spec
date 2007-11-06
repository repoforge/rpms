# $Id$
# Authority: dries
# Upstream: Sergey V. Kolychev <ksv$al,lg,ua>

%{?dist: %{expand: %%define %dist 1}}

%{!?dist:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-RawIP

Summary: Manipulate raw ip packets with interface to libpcap
Name: perl-Net-RawIP
Version: 0.2
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-RawIP/

Source: http://search.cpan.org/CPAN/authors/id/S/SK/SKOLYCHEV/Net-RawIP-%{version}.tar.gz
Patch: gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, libpcap, perl(ExtUtils::MakeMaker)
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
This is Net::RawIP, a perl module can to manipulate raw IP packets,
with an optional feature for manipulating Ethernet headers.

%prep
%setup -n %{real_name}-%{version}
%patch -p1

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} OPTIMIZE="%{optflags}"
#%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/RawIP/
%{perl_vendorarch}/Net/RawIP.pm
%dir %{perl_vendorarch}/auto/Net
%{perl_vendorarch}/auto/Net/RawIP/

%changelog
* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-2
- Gcc fixes: patch added.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
