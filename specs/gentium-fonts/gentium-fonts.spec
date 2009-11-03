# $Id$
# Authority: dag

# Dist: nodist

%define real_name ttf-sil-gentium

Summary: SIL Gentium fonts
Name: gentium-fonts
Version: 1.02
Release: 1%{?dist}
License: SIL Open Font License
Group: User Interface/X
#URL: http://scripts.sil.org/Gentium
URL: http://scripts.sil.org/Gentium_linux

#Source: http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=Gentium_102_L_tar&filename=%2Fttf-sil-gentium_1.0.2.tar.gz
Source: ttf-sil-gentium_1.0.2.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Obsoletes: fonts-sil-gentium
Provides: fonts-sil-gentium

%description
SIL Gentium ("belonging to the nations" in Latin) is a Unicode typeface family
designed to enable the many diverse ethnic groups around the world who use
the Latin script to produce readable, high-quality publications. It supports
a wide range of Latin-based alphabets and includes glyphs that correspond to
all the Latin ranges of Unicode.

%prep
%setup -n %{real_name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/fonts/gentium/
%{__install} -p -m0644 *.ttf %{buildroot}%{_datadir}/fonts/gentium/

touch %{buildroot}%{_datadir}/fonts/gentium/fonts.cache-1

%post
%{_bindir}/fc-cache -f %{_datadir}/fonts/gentium/ || :

%postun
if [ $1 -eq 0 ]; then
    %{_bindir}/fc-cache -f %{_datadir}/fonts/gentium/ || :
fi

%files
%defattr(-, root, root, 0755)
%doc FONTLOG GENTIUM-FAQ OFL OFL-FAQ QUOTES README
%dir %{_datadir}/fonts/
%dir %{_datadir}/fonts/gentium/
%{_datadir}/fonts/gentium/*.ttf
%ghost %{_datadir}/fonts/gentium/fonts.cache-1

%changelog
* Fri Sep 28 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
