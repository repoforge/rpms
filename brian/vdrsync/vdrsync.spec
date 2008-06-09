Name:           vdrsync
Version:        0.1.3
Release:        6.PRE1.050322%{?dist}
Summary:        Recording demultiplexer for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://vdrsync.vdr-portal.de/
Source0:        http://vdrsync.vdr-portal.de/releases/%{name}-%{version}PRE1.tgz
Source1:        http://vdrsync.vdr-portal.de/releases/%{name}-050322.tgz
Patch0:         %{name}-recpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       bitstream-vera-fonts
Requires:       dvdauthor
Requires:       ffmpeg
Requires:       m2vrequantiser
Requires:       mjpegtools
Requires:       mkisofs

%description
vdrsync is a script that demultiplexes VDR recordings and tries to
synchronize the video and audio streams by addition or deletion of
audio data. It can also start some other tools at the end of a run to
generate a video DVD Directory structure that can be burned on a DVD.


%prep
%setup -q -n %{name}-%{version}PRE1 -a1
mv vdrsync-050322/*.pl vdrsync-050322/CHANGES . ; rm -rf  vdrsync-050322
%patch0
for f in README.dvd-menu MANUAL-DE ; do
  iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done
rename .pl "" *.pl
%{__perl} -pi -e 's/(vdrsync(_buffer)?|dvd-menu)\.pl/$1/g' *
%{__perl} -pi -e 's|vdrsync_buffer|%{_datadir}/vdrsync/vdrsync_buffer|' \
  vdrsync
%{__perl} -pi -e 's|/usr/X11R6/lib/X11/fonts/truetype/arial.ttf|%{_datadir}/fonts/bitstream-vera/Vera.ttf| ; s/arial.ttf/Vera.ttf/' *dvd-menu*


%build


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 vdrsync dvd-menu $RPM_BUILD_ROOT%{_bindir}
install -Dpm 755 vdrsync_buffer \
  $RPM_BUILD_ROOT%{_datadir}/vdrsync/vdrsync_buffer


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc BUGS CHANGES COPYING MANUAL README* TODO
%lang(de) %doc MANUAL-DE
%{_bindir}/vdrsync
%{_bindir}/dvd-menu
%{_datadir}/vdrsync/


%changelog
* Fri Oct 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-6.PRE1.050322
- Use m2vrequantiser instead of transcode.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.1.3-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-4.PRE1.050322
- Rebuild.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.1.3-3.PRE1.050322
- drop 1.lvn from release

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-1.lvn.3.PRE1.050322
- Fix missing dir separator in recording paths.

* Sun Aug 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-1.lvn.2.PRE1.050322
- 050322 snapshot, cleanup patch applied upstream.

* Fri Aug 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-1.lvn.1.PRE1
- Convert docs to UTF-8.

* Sat Jun 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-0.2.PRE1
- Rebuild for FC4.

* Mon Jan 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.1.3-0.1.PRE1
- Update to 0.1.3PRE1.

* Sun Dec 26 2004 Ville Skyttä <ville.skytta at iki.fi> - 0.1.2.2-0.2
- Remove unnecessary Epochs.

* Sun Nov 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.2.2-0.scop.1
- First build.
