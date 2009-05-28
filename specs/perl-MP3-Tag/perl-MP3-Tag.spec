# $Id$
# Authority: dag
# Upstream: Ilya Zakharevich <cpan$ilyaz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MP3-Tag

Summary: Module for reading tags of MP3 audio files
Name: perl-MP3-Tag
Version: 1.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MP3-Tag/

Source: http://www.cpan.org/modules/by-module/MP3/MP3-Tag-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Module for reading tags of MP3 audio files.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README.shrink README.txt TODO examples/
%doc %{_mandir}/man1/audio_rename.1*
%doc %{_mandir}/man1/mp3info2.1*
%doc %{_mandir}/man1/typeset_audio_dir.1*
%doc %{_mandir}/man3/MP3::Tag.3pm*
%doc %{_mandir}/man3/MP3::Tag::*.3pm*
%doc %{_mandir}/man3/Normalize::Text::Music_Fields.3pm*
%{_bindir}/audio_rename
%{_bindir}/mp3info2
%{_bindir}/typeset_audio_dir
%dir %{perl_vendorlib}/MP3/
%{perl_vendorlib}/MP3/Tag/
%{perl_vendorlib}/MP3/Tag.pm
%{perl_vendorlib}/Normalize/Text/Music_Fields.pm
%{perl_vendorlib}/Normalize/Text/Music_Fields/
%{perl_vendorlib}/Encode/transliterate_win1251.pm

%changelog
* Thu Aug 28 2009 Christoph Maser <cmr@financial.com> 1.11-1
- Update to version 1.11.

* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 0.9710-1
- Initial package. (using DAR)
