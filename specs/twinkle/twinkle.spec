# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: SIP soft phone
Name: twinkle
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.twinklephone.com/

Source: http://www.xs4all.nl/~mfnboer/twinkle/download/twinkle-%{version}.tar.gz
Patch0: twinkle-1.1-msg.patch
Patch1: twinkle-1.2-gcc43.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: alsa-lib-devel
BuildRequires: bind-devel
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: ccrtp-devel
BuildRequires: commoncpp2-devel
BuildRequires: desktop-file-utils
BuildRequires: kdelibs-devel
BuildRequires: libsndfile-devel
BuildRequires: qt-devel
BuildRequires: speex-devel

%description
Twinkle is a SIP based soft phone for making telephone calls over IP networks.

%prep
%setup
%patch0 -p1 -b .msg
#patch1 -p1 -b .gcc43

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 src/gui/images/twinkle48.png %{buildroot}%{_datadir}/pixmaps/twinkle.png

desktop-file-install --vendor %{desktop_vendor}    \
        --dir %{buildroot}%{_datadir}/applications \
        twinkle.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/twinkle
%{_datadir}/applications/%{desktop_vendor}-twinkle.desktop
%{_datadir}/pixmaps/twinkle.png
%{_datadir}/twinkle/

%changelog
* Sun Sep 14 2008 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAG)
