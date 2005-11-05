# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Kwiki

Summary: Kwiki module for perl
Name: perl-Kwiki
Version: 0.38
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
#URL: http://search.cpan.org/dist/Kwiki/
URL: http://www.kwiki.org/

Source: http://www.cpan.org/modules/by-module/Kwiki/Kwiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Kwiki is a modular implementation of a Wiki in Perl.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
        PREFIX="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor" \
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
%doc Changes README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/*
%{_bindir}/*

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Thu Sep 30 2004 Dag Wieers <dag@wieers.com> - 0.33-1
- Initial package. (using DAR)
