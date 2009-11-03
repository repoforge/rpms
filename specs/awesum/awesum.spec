# $Id$
# Authority: dag
# Upstream: Darren L. LaChausse <the_trapper$users,sourceforge,net>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Graphical checksum verifier
Name: awesum
Version: 0.6.0
Release: 1.2%{?dist}
License: BSD
Group: Applications/File
URL: http://awesum.sourceforge.net/

Source: http://dl.sf.net/awesum/awesum-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python, pygtk2
Requires: python, pygtk2
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Awesum is a graphical checksum verification utility. Awesum is very easy to
use and includes support for both MD5 and SHA checksum algorithms. Unlike
many checksum verification utilities, Awesum features a progress bar which
makes working with large files (such as CD-ROM ISO images) much more bearable.

%prep
%setup -n %{name}

%{__cat} <<EOF >awesum.desktop
[Desktop Entry]
Name=Checksum Verifier
Comment=Verify the checksum of files
Icon=redhat-accessories.png
Exec=awesum
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Utility;
EOF

%build

%install
%{__rm} -rf %{buildroot}
./install.sh

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	awesum.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/awesum/*.txt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt doc/html/
%{_bindir}/awesum
%{_datadir}/applications/%{desktop_vendor}-awesum.desktop
%{_datadir}/awesum/
%exclude %{_docdir}/awesum/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1.2
- Rebuild for Fedora Core 5.

* Tue May 04 2004 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Initial package. (using DAR)
