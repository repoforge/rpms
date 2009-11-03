# $Id$
# Authority: dag

# Dist: nodist

%define real_name MgOpen
%define real_version 20050515

Summary: Truetype greek fonts
Name: mgopen-fonts
Version: 0.20050515
Release: 1%{?dist}
License: Bitstream Vera
Group: User Interface/X
URL: http://www.ellak.gr/fonts/mgopen/

### Source0: http://www.ellak.gr/fonts/mgopen/files/MgOpen.tar.gz
Source: MgOpen-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# Conflicts: fontconfig < 2.3.93

%description
The MgOpen fonts are a font family that includes Latin and Greek glyphs.
The fonts have been released under a liberal license, similar to the
license covering the Bitstream Vera fonts.

%prep
%setup -c

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/fonts/mgopen/
%{__install} -p -m0644 *.ttf  %{buildroot}%{_datadir}/fonts/mgopen/

%clean
%{__rm} -rf %{buildroot}

%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache -r %{_datadir}/fonts/mgopen/ || :
fi

%postun
if [ $1 -eq 0 ]; then
    if [ -x %{_bindir}/fc-cache ]; then
        %{_bindir}/fc-cache -f %{_datadir}/fonts/mgopen/ || :
    fi
fi

%files
%defattr(-, root, root, 0755)
%{_datadir}/fonts/mgopen/

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.20050515-1
- Initial package. (based on fedora)
