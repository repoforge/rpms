# $Id$
# Authority: dries
# Upstream: Nick Peskett <npeskett$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Audio-CoolEdit

Summary: Read and write Syntrillium CoolEdit Pro .ses files
Name: perl-Audio-CoolEdit
Version: 0.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Audio-CoolEdit/

Source: http://search.cpan.org/CPAN/authors/id/N/NP/NPESKETT/Audio-CoolEdit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Modules for reading & writing Syntrillium CoolEdit Pro .ses files.

Syntrillium's CoolEdit Pro (http://www.syntrillium.com) is a
MSWin32 based multitrack capable sound editor. This module
reads/ writes the .ses (session) file format enabling you to
place audio files in a vitual track at a given offset. The write
module is a lot more developed than the read module as this has
been developed to be used with Audio::Mix.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Audio/CoolEdit.pm
%{perl_vendorlib}/Audio/CoolEdit
%{perl_vendorlib}/Audio/makewavs.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
